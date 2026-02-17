import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
    name: 'reverse'
})

export class ReversePipe implements PipeTransform {
    transform(value: string): string {
        let letters = value.split('');
        let reverse = new Array();

        for (let letter of letters) {
            reverse.unshift(letter);
        };

        let result = reverse.join('');
        return result;
    };
}