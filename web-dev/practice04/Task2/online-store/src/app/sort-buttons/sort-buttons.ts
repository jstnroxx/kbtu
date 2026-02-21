import { Component, output } from '@angular/core';

@Component({
  selector: 'app-sort-buttons',
  imports: [],
  templateUrl: './sort-buttons.html',
  styleUrl: './sort-buttons.css',
})
export class SortButtons {
    passSortType = output<string>();
    currentSortType = 'default';

    sortList(type: string) {
        if (type === this.currentSortType) {
            this.passSortType.emit('default');
            this.currentSortType = 'default';
            return;
        }

        if (type === 'asc') {
            this.passSortType.emit('asc');
        } else if (type === 'desc') {
            this.passSortType.emit('desc');
        } else {
            this.passSortType.emit('default');
            this.currentSortType = 'default';
            return;
        };

        this.currentSortType = type;
    };
}
