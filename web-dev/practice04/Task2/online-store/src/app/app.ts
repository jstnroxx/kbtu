import { Component, signal } from '@angular/core';
import { ProductList } from './product-list/product-list';
import { SortButtons } from "./sort-buttons/sort-buttons";

@Component({
    selector: 'app-root',
    imports: [ProductList, SortButtons],
    templateUrl: './app.html',
    styleUrl: './app.css'
})
export class App {
    protected readonly title = signal('online-store');

    sortTypeToPass = 'default';

    handlePassedSortType(event: string) {
        this.sortTypeToPass = event;
    };
}
