from __future__ import annotations

import psycopg2

from config import load_db_config


# Connection helper
def _connect():
    params = load_db_config()
    
    return psycopg2.connect(**params)


# Schema bootstrap
def ensure_schema() -> None:
    ddl = """
        CREATE TABLE IF NOT EXISTS players (
            id       SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
        CREATE TABLE IF NOT EXISTS game_sessions (
            id            SERIAL PRIMARY KEY,
            player_id     INTEGER REFERENCES players(id),
            score         INTEGER   NOT NULL,
            level_reached INTEGER   NOT NULL,
            played_at     TIMESTAMP DEFAULT NOW()
        );
    """
    
    try:
        conn = _connect()
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(ddl)
        conn.close()
    except Exception as exc:
        print(f"[db] ensure_schema failed: {exc}")


# Player helpers
def get_or_create_player(username: str) -> int | None:
    try:
        conn = _connect()
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO players (username) VALUES (%s) "
                    "ON CONFLICT (username) DO NOTHING;",
                    (username,)
                )
                cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
                row = cur.fetchone()
        conn.close()
        
        return row[0] if row else None
    except Exception as exc:
        print(f"[db] get_or_create_player failed: {exc}")
        
        return None


# Session helpers
def save_session(player_id: int, score: int, level_reached: int) -> None:
    try:
        conn = _connect()
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO game_sessions (player_id, score, level_reached) "
                    "VALUES (%s, %s, %s);",
                    (player_id, score, level_reached)
                )
        conn.close()
    except Exception as exc:
        print(f"[db] save_session failed: {exc}")


def get_personal_best(player_id: int) -> int:
    try:
        conn = _connect()
        
        with conn.cursor() as cur:
            cur.execute(
                "SELECT COALESCE(MAX(score), 0) FROM game_sessions WHERE player_id = %s;",
                (player_id,)
            )
            row = cur.fetchone()
        conn.close()
        
        return row[0] if row else 0
    except Exception as exc:
        print(f"[db] get_personal_best failed: {exc}")
        
        return 0


def get_leaderboard(limit: int = 10) -> list[tuple]:
    query = """
        SELECT
            ROW_NUMBER() OVER (ORDER BY gs.score DESC) AS rank,
            p.username,
            gs.score,
            gs.level_reached,
            gs.played_at
        FROM game_sessions gs
        JOIN players p ON p.id = gs.player_id
        ORDER BY gs.score DESC
        LIMIT %s;
    """
    try:
        conn = _connect()
        
        with conn.cursor() as cur:
            cur.execute(query, (limit,))
            rows = cur.fetchall()
        conn.close()
        
        return rows
    except Exception as exc:
        print(f"[db] get_leaderboard failed: {exc}")
        
        return []