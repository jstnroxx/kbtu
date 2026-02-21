export interface ProductModel {
    id: number,
    name: string,
    categoryId: number,
    description: string,
    price: number,
    rating: number,
    likes: number,
    image: string,
    images: string[],
    link: string
}