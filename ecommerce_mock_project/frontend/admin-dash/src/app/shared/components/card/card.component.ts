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
   * Inputs for background and height classes, since default card doesn't
   * specify those for the sake of modularity
   */
  @Input() backgroundClass: string = '';
  @Input() height: string = '';
  @Input() opacity: boolean = true;
  @Input() textColor: string = 'text-white';

  getCombinedClasses() {
    return { [this.backgroundClass]: true, 'opacity-20': this.opacity };
  }
}
