import { Component } from '@angular/core';
import { ProductList } from './product-list/product-list';
import { NavButtons } from './nav-buttons/nav-buttons';
import { CategoryModel } from './data-interfaces/category-model/category.model';
import { ProductManipulatorModel } from './data-interfaces/product-manipulator-model/product.manipulator.model';
import { SubCategoryModel } from './data-interfaces/category-model/sub.category.model';
import jsonCategorizedProducts from '../../public/formatted-json-products.json';

@Component({
    selector: 'app-root',
    imports: [ProductList, NavButtons],
    templateUrl: './app.html',
    styleUrl: './app.css'
})
export class App {
    categorizedProducts: CategoryModel[] = [];
    productCategories: SubCategoryModel[] = [];

    constructor() {
        const storedProducts = localStorage.getItem('productList');

        if (storedProducts === null) {
            this.categorizedProducts = structuredClone(jsonCategorizedProducts);
        } else {
            this.categorizedProducts = JSON.parse(storedProducts);
        };

        this.productCategories = this.categorizedProducts.map(({ id, name }) => ({ id, name}));
    };
    
    categoryProducts: CategoryModel[] = [];         

    storeProducts() {
        localStorage.setItem('productList', JSON.stringify(this.categorizedProducts));
    };

    updateLikeCount(event: ProductManipulatorModel) {
        const productCategory = this.categorizedProducts.find(category => category.id === event.categoryId);
        const productObject = productCategory?.products.find(product => product.id === event.productId);
        
        if (productObject?.likes !== undefined) {
            if (event.likeCount === -1) {
                const productIndex = productCategory?.products.findIndex(product => product === productObject) ?? 0;

                productCategory?.products.splice(productIndex, 1)
            } else {
                productObject.likes = event.likeCount;
            };
        };

        this.storeProducts();
    };

    handleRedirect(event: number) {
        this.categoryProducts = this.categorizedProducts.filter(obj => obj.id === event);
        console.log(this.productCategories);
    };

    handleRestore() {
        this.categorizedProducts = structuredClone(jsonCategorizedProducts);
        localStorage.removeItem('productList');
    };
}
