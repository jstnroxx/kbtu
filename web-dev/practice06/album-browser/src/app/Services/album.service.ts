import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Album } from '../Interfaces/album.model';
import { Photo } from '../Interfaces/photo.model';

@Injectable({
    providedIn: 'root'
})

export class AlbumService {
    private http = inject(HttpClient);

    getAlbums(): Observable<Album[]> {
        return this.http.get<Album[]>('https://jsonplaceholder.typicode.com/albums');
    };

    getAlbum(id: number): Observable<Album> {
        return this.http.get<Album>(`https://jsonplaceholder.typicode.com/albums/${id}`);
    };

    getAlbumPhotos(id: number): Observable<Photo[]> {
        return this.http.get<Photo[]>(`https://jsonplaceholder.typicode.com/albums/${id}/photos`);
    };

    updateAlbum(album: Album): Observable<Album> {
        return this.http.put<Album>(`https://jsonplaceholder.typicode.com/albums/${album.id}`, album);
    };

    deleteAlbum(id: number): Observable<void> {
        return this.http.delete<void>(`https://jsonplaceholder.typicode.com/albums/${id}`);
    };
}