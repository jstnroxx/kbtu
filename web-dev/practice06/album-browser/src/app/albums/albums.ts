import { Component, signal, OnInit } from '@angular/core';
import { AlbumService } from '../Services/album.service';
import { Album } from '../Interfaces/album.model';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-albums',
  imports: [RouterLink],
  templateUrl: './albums.html',
  styleUrl: './albums.css',
})
export class Albums implements OnInit {
    allAlbums = signal<Album[] | undefined>(undefined);

    constructor(private albumService: AlbumService) {};

    ngOnInit(): void {
        this.albumService.getAlbums().subscribe(albums => {
            this.allAlbums.set(albums);
        });
    };

    deleteAlbum(albumId: number) {
        this.albumService.deleteAlbum(albumId).subscribe({
            complete: () => {
                this.allAlbums.set(this.allAlbums()?.filter(album => album.id != albumId));
            }
        });
    };

    deleteAllAlbums() {
        if (this.allAlbums()) {
            for (let album of this.allAlbums() ?? []) {
                this.deleteAlbum(album.id);
            }
        } else {
            return
        }
    };
}
