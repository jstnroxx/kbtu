import { Component, OnInit, signal } from '@angular/core';
import { AlbumService } from '../Services/album.service';
import { Album } from '../Interfaces/album.model';
import { RouterLink, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-album-detail',
  imports: [RouterLink],
  templateUrl: './album-detail.html',
  styleUrl: './album-detail.css',
})
export class AlbumDetail implements OnInit {
    currentAlbumId: number = 0;
    currentAlbum = signal<Album>({
        userId: 0,
        id: 0,
        title: ''
    });
    albumTitleTo = '';

    constructor(
        private currentRoute: ActivatedRoute, 
        private albumService: AlbumService
    ) {};

    ngOnInit(): void {
        this.currentAlbumId = Number(this.currentRoute.snapshot.paramMap.get('id'));

        this.albumService.getAlbum(this.currentAlbumId).subscribe(album => {
            this.currentAlbum.set(album)
            this.albumTitleTo = album.title;
        });
    };

    updateTitleInput(input: string) {
        this.albumTitleTo = input
    };

    setTitle() {
        let tempAlbum: Album = {
            userId: this.currentAlbum().userId,
            id: this.currentAlbum().id,
            title: this.albumTitleTo
        };
        this.albumService.updateAlbum(tempAlbum).subscribe({
            complete: () => {
                this.currentAlbum.set(tempAlbum);
            }
        });
    };
}
