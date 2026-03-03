import { Routes } from '@angular/router';
import { Home } from './home/home';
import { About } from './about/about';
import { Albums } from './albums/albums';
import { AlbumDetail } from './album-detail/album-detail';
import { AlbumPhotos } from './album-photos/album-photos';
import { NotFound } from './not-found/not-found'; 

export const routes: Routes = [
    {
        path: '',
        redirectTo: '/home',
        pathMatch: 'full'
    },
    {
        path: 'home',
        component: Home,
        title: 'Album Browser'
    },
    {
        path: 'about',
        component: About,
        title: 'About'
    },
    {
        path: 'albums',
        component: Albums,
        title: 'Albums'
    },
    {
        path: 'albums/:id',
        component: AlbumDetail,
    },
    {
        path: 'albums/:id/photos',
        component: AlbumPhotos
    },
    {
        path: '**',
        component: NotFound,
        title: 'Not Found'
    }
];
