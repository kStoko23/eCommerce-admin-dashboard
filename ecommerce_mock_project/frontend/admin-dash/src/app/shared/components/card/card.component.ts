import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './card.component.html',
  styleUrl: './card.component.css',
})
export class CardComponent {
  /*
   * Inputs for background, height, text color classes, since default card doesn't
   * specify those for the sake of modularity
   */
  @Input() backgroundClass: string = 'bg-[rgba(67,_67,_67,_0.2)]';
  @Input() height: string = 'h-1/2 lg:h-full';
  @Input() textColor: string = 'text-white';

  getCombinedClasses() {
    return {
      [this.backgroundClass]: true,
      [this.height]: true,
      [this.textColor]: true,
    };
  }
}
