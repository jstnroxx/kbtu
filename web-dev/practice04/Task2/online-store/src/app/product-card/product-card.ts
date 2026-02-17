import { Component, input, linkedSignal, computed } from '@angular/core';
import { ProductModel } from '../product-model/product.model';
import { DecimalPipe } from '@angular/common';

@Component({
  selector: 'app-product-card',
  imports: [DecimalPipe],
  templateUrl: './product-card.html',
  styleUrl: './product-card.css',
})
export class ProductCard {
    productObject = input<ProductModel>();

    currentImageIndex = linkedSignal({
        source: this.productObject,
        computation: () => -1
    });
    
    currentImagePath = computed(() => {
        const product = this.productObject();
        const images = product?.images || [];
        
        return this.currentImageIndex() >= 0 ? images[this.currentImageIndex()] : product?.image;
    });


    redirectTo(url: string) {
        if (url != "") {
            window.open(url, '_blank');
        } else {
            window.location.href = '#';
        }
    };

    isThumbnailControl = false;

    showControls() {
        this.isThumbnailControl = true;
    };

    hideControls() {
        this.isThumbnailControl = false;
        this.currentImageIndex.set(-1);
    };

    nextThumbnail() {
        const images = this.productObject()?.images || [];
        if (images.length === 0) return;

        this.currentImageIndex.update(currentIndex => (currentIndex + 1) % images.length);
    };

    previousThumbnail() {
        const images = this.productObject()?.images || [];
        if (images.length === 0) return;

        this.currentImageIndex.update(currentIndex => (currentIndex - 1 + images.length) % images.length);
    };

    shareProduct() {
        const productLink = this.productObject()?.link ?? '';
        const encodedLink = encodeURIComponent(productLink);

        window.open('https://wa.me/?text=Check out this product: ' + encodedLink, '_blank');
    };
}
