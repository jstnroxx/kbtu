import { Component } from '@angular/core';
import { User } from './user/user';
import { Child } from './child/child';
import { NgOptimizedImage } from '@angular/common';
import { RouterOutlet, RouterLink } from '@angular/router';
import { FormGroup, FormControl } from '@angular/forms';
import { ReactiveFormsModule, Validators } from '@angular/forms';
import { inject } from '@angular/core';
import { CarService } from './car-service/car.service';
import { LowerCasePipe } from '@angular/common';
import { DecimalPipe, DatePipe, CurrencyPipe } from '@angular/common';
import { ReversePipe } from './reverse-pipe/reverse.pipe';

@Component({
    selector: 'app-demoUser',
    template: `
        Username: {{ username }}
    `
})
export class DemoUser {
    username = 'Maxim';
}

@Component({
    selector: 'app-root',
    template: `
        Hello {{ city }}, {{ 1 + 1 }}

        <section>
            <app-demoUser/>
        </section>

        @if (isServerRunning) {
            <span>Yes, the server is running</span>
        } @else {
            <span>No, the server is not running</span>
        }
        
        @for (user of users; track user.id) {
            <p>{{ user.name }}</p>
        }

        <div [contentEditable]="isEditable">
            Hello!
        </div>

        <section (mouseover)="showSecret()">
            There's a secret message for you, hover to reveal: {{ message }}
        </section>

        <app-user name="Maxim S."/>

        <br>
        <app-child (addItemEvent)="addItem($event)"/>
        <p>🐢 all the way down {{ items.length }}</p>

        @defer (on viewport) {
            <p>
                Some comments.
            </p>
        } @placeholder {
            <p>
                Some placeholder.
            </p>
        } @loading (minimum 2s) {
            <p>
                Some loading...
            </p>
        }

        <p>Preferred Framework:</p>
        <ul>
            <li>
                Static Image:
                <img src="/favicon.ico" alt="Angular icon" width="32px" height="32px"/>
            </li>
            <li>
                Dynamic Image:
                <img [ngSrc]="logoPath" [alt]="logoAlt" width="32" height="32"/>
            </li>
        </ul>

        <nav>
            <a routerLink="/">Home</a>
            |
            <a routerLink="/user">User</a>
        </nav>
        <router-outlet/>

        <br><br>
        <form [formGroup]="profileForm" (ngSubmit)="handleSubmit()">
            <input type="text" formControlName="name" />
            <input type="email" formControlName="email" />

            <button type="submit" [disabled]="!profileForm.valid">Submit</button>
        </form>

        <h2>Profile Form</h2>
        <p>
            Name: {{ profileForm.value.name }}
        </p>
        <p>
            Email: {{ profileForm.value.email }}
        </p>

        <p>
            Some cars: {{ carDisplay }}
        </p>

        {{ username | lowercase}}

        <ul>
            <li>Number with "decimal" {{ num | number: '3.2-2'}}</li>
            <li>Date with "date" {{ birthday | date: 'medium'}}</li>
            <li>Currency with "currency" {{ cost | currency: 'KZT'}}</li>
        </ul>

        {{ someMessage }} reversed is: {{ someMessage | reverse }}
    `,
    imports: [DemoUser, User, Child, NgOptimizedImage, RouterOutlet, RouterLink, ReactiveFormsModule, LowerCasePipe, DecimalPipe, DatePipe, CurrencyPipe, ReversePipe]
})
export class App {
    city = "San Francisco";

    isServerRunning = true;

    users = [
        {id: 0, name: 'Sarah'},
        {id: 1, name: 'Amy'},
        {id: 2, name: 'Rachel'},
        {id: 3, name: 'Jessica'},
        {id: 4, name: 'Poornima'},
    ];

    isEditable = true;

    message = "";
    showSecret() {
        this.message = "Way to go 🚀";
    };

    items = new Array();
    addItem(item: string) {
        this.items.push(item);
    };

    logoPath = '/favicon.ico';
    logoAlt = 'Angular icon';

    profileForm = new FormGroup({
        name: new FormControl('', Validators.required),
        email: new FormControl('', [Validators.required, Validators.email]),
    });
    handleSubmit() {
        alert(this.profileForm.value.name + ' | ' + this.profileForm.value.email);
    };

    carService = inject(CarService);
    carDisplay = this.carService.getCars().join(' ⭐ ');

    username = 'mAxIm!!!';

    num = 103.1234;
    birthday = new Date(2023, 3, 2);
    cost = 4560.34;

    someMessage = 'this is a message.';
}
