import { Component } from '@angular/core';
import { ProductList } from './product-list/product-list';
import { CategoryModel } from './data-interfaces/category-model/category.model';
import { ProductManipulatorModel } from './data-interfaces/product-manipulator-model/product.manipulator.model';
import jsonCategorizedProducts from '../../public/categorized-products.json';

@Component({
    selector: 'app-root',
    imports: [ProductList],
    templateUrl: './app.html',
    styleUrl: './app.css'
})
export class App {
    categorizedProducts: CategoryModel[] = jsonCategorizedProducts;
    
    categoryIndex = 0;           // Implement category navigation

    updateLikeCount(event: ProductManipulatorModel) {
        const productCategory = this.categorizedProducts.find(category => category.id === event.categoryId)
        const productObject = productCategory?.products.find(product => product.id === event.productId)
        
        if (productObject?.likes !== undefined) {
            if (event.likeCount === -1) {
                const productIndex = productCategory?.products.findIndex(product => product === productObject) ?? 0
                
                productCategory?.products.splice(productIndex, 1)
            } else {
                productObject.likes = event.likeCount;
            }
        };
    };
}
