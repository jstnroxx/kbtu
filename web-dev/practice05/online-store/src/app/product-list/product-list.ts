import { Component, signal, effect, input, output } from '@angular/core';
import { ProductCard } from '../product-card/product-card';
import { SortButtons } from '../sort-buttons/sort-buttons';
import { ProductModel } from '../data-interfaces/product-model/product.model';
import { ProductManipulatorModel } from '../data-interfaces/product-manipulator-model/product.manipulator.model';

@Component({
  selector: 'app-product-list',
  imports: [ProductCard, SortButtons],
  templateUrl: './product-list.html',
  styleUrl: './product-list.css',
})
export class ProductList {
    products = input<ProductModel[]>([])

    sendLike = output<ProductManipulatorModel>();

    receivedSortType = signal('default');

    receiveSortType(event: string) {
        this.receivedSortType.set(event);
    };

    sortList(type: string) {
        if (type === 'asc') {
            this.products().sort((card1, card2) => card1.price - card2.price);
        } else if (type === 'desc') {
            this.products().sort((card1, card2) => card2.price - card1.price);
        } else if (type === 'default') {
            this.products().sort((card1, card2) => card1.id - card2.id);
        } else {
            alert("Something went wrong when sorting.");
            return;
        };
    };

    constructor() {
        effect(() => {
            this.sortList(this.receivedSortType() ?? 'default');
        });
    };

    receiveLike(event: ProductManipulatorModel) {
        this.sendLike.emit(event);
    };
}
