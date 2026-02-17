import { Component, input } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-user',
    template: `
		<p>
			Username: {{ username }} <br>
			The user's name is {{ name() }}
    	</p>

        <p>
            {{ username }}'s favorite framework: {{ favoriteFramework }}
        </p>

        <label for="framework">
            Favorite framework:

            <input id="framework" type="text" [(ngModel)]="favoriteFramework"/>
        </label>
        <button (click)="showFramework()">Show Framework</button>
    `,
    imports: [FormsModule]
})
export class User {
    username = 'Maxim';
	name = input<string>();
    favoriteFramework = '';
    showFramework() {
        alert(this.favoriteFramework );
    };
}
