import { Component, OnInit, signal } from '@angular/core';
import { RouterLink, ActivatedRoute } from '@angular/router';
import { AlbumService } from '../Services/album.service';
import { Photo } from '../Interfaces/photo.model';

@Component({
  selector: 'app-album-photos',
  imports: [RouterLink],
  templateUrl: './album-photos.html',
  styleUrl: './album-photos.css',
})
export class AlbumPhotos implements OnInit {
    albumId: number = 0;
    albumPhotos = signal<Photo[]>([]);

    constructor(
        private currentRoute: ActivatedRoute,
        private albumService: AlbumService
    ) {};

    ngOnInit(): void {
        this.albumId = Number(this.currentRoute.snapshot.paramMap.get('id'));
        
        this.albumService.getAlbumPhotos(this.albumId).subscribe(photos => {
            this.albumPhotos.set(photos);
        });
    }
}
