import { Component, input, effect } from '@angular/core';
import { ProductCard } from '../product-card/product-card';
import { ProductModel } from '../product-model/product.model';

@Component({
  selector: 'app-product-list',
  imports: [ProductCard],
  templateUrl: './product-list.html',
  styleUrl: './product-list.css',
})
export class ProductList {
    receivedSortType = input<string>();

    sortList(type: string) {
        if (type === 'asc') {
            this.products.sort((card1, card2) => card1.price - card2.price);
        } else if (type === 'desc') {
            this.products.sort((card1, card2) => card2.price - card1.price);
        } else if (type === 'default') {
            this.products.sort((card1, card2) => card1.id - card2.id);
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

    products: ProductModel[] = [
        {
            id: 0,
            name: "iPhone 17 Pro 256Gb",
            description: "The iPhone 17 is a smartphone developed and marketed by Apple that is part of the nineteenth generation of the iPhone.",
            price: 774648,
            rating: 5,
            image: "./images/iphone17/iphone17.jpg",
            images: ["./images/iphone17/iphone17_1.jpg", "./images/iphone17/iphone17_2.jpg", "./images/iphone17/iphone17_3.jpg"],
            link: "https://kaspi.kz/shop/p/apple-iphone-17-pro-256gb-oranzhevyi-145467625"
        },
        {
            id: 1,
            name: "Giant Glory Advanced - 2023",
            description: "The heart of the Glory Advanced is a lightweight, super-strong chassis that's handcrafted with Advanced-grade composite.",
            price: 3499900,
            rating: 0,
            image: "./images/giant/giant.jpg",
            images: ["./images/giant/giant_1.jpg", "./images/giant/giant_2.jpg", "./images/giant/giant_3.jpg"],
            link: "https://kaspi.kz/shop/p/velosiped-giant-glory-advanced---2023-29-djuim-2023-18-5-djuimov-belyi-121119182"
        },
        {
            id: 2,
            name: "Apple Watch Ultra Series 2",
            description: "The Apple Watch Ultra 2 is a rugged 49mm smartwatch designed for athletes and outdoor enthusiasts.",
            price: 553322,
            rating: 5,
            image: "./images/watch/watch.jpg",
            images: ["./images/watch/watch_1.jpg", "./images/watch/watch_2.jpg", "./images/watch/watch_3.jpg"],
            link: "https://kaspi.kz/shop/p/apple-watch-ultra-series-2-gps-cellular-49-mm-starlight-sinii-113573988"
        },
        {
            id: 3,
            name: "Xiaomi Redmi Power Bank",
            description: "Xiaomi power banks are compact, high-efficiency portable chargers, often featuring 10,000mAh to 20,000mAh capacities.",
            price: 4096,
            rating: 4,
            image: "./images/xiaomi/xiaomi.jpg",
            images: ["./images/xiaomi/xiaomi_1.jpg", "./images/xiaomi/xiaomi_2.jpg", "./images/xiaomi/xiaomi_3.jpg"],
            link: "https://kaspi.kz/shop/p/vneshnii-akkumuljator-xiaomi-redmi-power-bank-20000-mach-18-vt-chernyi-100322086"
        },
        {
            id: 4,
            name: "Razer BlackWidow V3",
            description: "The name that started it all returns to reassert its dominance. Feel the difference with the Razer BlackWidow V3.",
            price: 43000,
            rating: 5,
            image: "./images/razer/razer.jpg",
            images: ["./images/razer/razer_1.jpg", "./images/razer/razer_2.jpg", "./images/razer/razer_3.jpg"],
            link: "https://kaspi.kz/shop/p/razer-blackwidow-v3-tenkeyless-rz03-03490700-r3r1-chernyi-101004900"
        },
        {
            id: 5,
            name: "Fifine AM8",
            description: "Get your voice clarity with FIFINE AmpliGame AM8 Microphone, a USB/XLR dynamic microphone.",
            price: 31999,
            rating: 5,
            image: "./images/fifine/fifine.jpg",
            images: ["./images/fifine/fifine_1.jpg", "./images/fifine/fifine_2.jpg", "./images/fifine/fifine_3.jpg"],
            link: "https://kaspi.kz/shop/p/mikrofon-fifine-am8-white-belyi-114268353"
        },
        {
            id: 6,
            name: "Jiangxihuitian",
            description: "A fedora is a timeless, soft-brimmed hat featuring an indented, 'pinched' crown.",
            price: 1861,
            rating: 5,
            image: "./images/hat/hat.jpg",
            images: ["./images/hat/hat_1.jpg", "./images/hat/hat_2.jpg"],
            link: "https://kaspi.kz/shop/p/shljapa-jiangxihuitian-ht1260-razmer-56-57-58-chernyi-104381002"
        },
        {
            id: 7,
            name: "MSI MAG255XF",
            description: "The MSI ARSENAL GAMING (MAG) series is engineered to give gamers the edge they need to dominate on the virtual battlefield.",
            price: 93989,
            rating: 5,
            image: "./images/msi/msi.jpg",
            images: ["./images/msi/msi_1.jpg", "./images/msi/msi_2.jpg", "./images/msi/msi_3.jpg"],
            link: "https://kaspi.kz/shop/p/24-5-msi-mag255xf-chernyi-131894370"
        },
        {
            id: 8,
            name: "Ledger Nano S Plus",
            description: "Securely manage 15000+ crypto with the classic Ledger Nano S Plus signer.",
            price: 60692,
            rating: 5,
            image: "./images/ledger/ledger.jpg",
            images: ["./images/ledger/ledger_1.jpg", "./images/ledger/ledger_2.jpg", "./images/ledger/ledger_3.jpg"],
            link: "https://kaspi.kz/shop/p/ledger-nano-s-plus-chernyi-106365043"
        },
        {
            id: 9,
            name: "ASUS TUF Gaming A15",
            description: "The ASUS TUF Gaming A15 is a durable, budget-friendly 15.6-inch gaming laptop.",
            price: 468757,
            rating: 4,
            image: "./images/asus/asus.jpg",
            images: ["./images/asus/asus_1.jpg", "./images/asus/asus_2.jpg", "./images/asus/asus_3.jpg"],
            link: "https://kaspi.kz/shop/p/asus-tuf-gaming-a15-15-6-16-gb-ssd-512-gb-bez-os-90nr0jf7-m00jd0-147782981"
        }
    ]
}
