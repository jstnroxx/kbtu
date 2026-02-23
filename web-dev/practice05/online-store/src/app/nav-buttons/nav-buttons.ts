import { Component, input, output } from '@angular/core';
import { SubCategoryModel } from '../data-interfaces/category-model/sub.category.model';

@Component({
  selector: 'app-nav-buttons',
  imports: [],
  templateUrl: './nav-buttons.html',
  styleUrl: './nav-buttons.css',
})
export class NavButtons {
    queryRestore = output();
    redirectToCategory = output<number>();

    categories = input<SubCategoryModel[]>([]);

    redirectTo(categoryId: number) {
        this.redirectToCategory.emit(categoryId);
    };

    restoreProducts() {
        this.queryRestore.emit();
    };
}
