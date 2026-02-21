import { ProductModel } from '../product-model/product.model';

export interface CategoryModel {
    id: number,
    name: string,
    products: ProductModel[]
}