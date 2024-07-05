import { Component } from '@angular/core';
import { CardComponent } from '../../shared/components/card/card.component';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-page-dashboard',
  standalone: true,
  imports: [CardComponent, CommonModule, RouterLink],
  templateUrl: './page-dashboard.component.html',
  styleUrl: './page-dashboard.component.css',
})
export class PageDashboardComponent {
  totalOrders: number = 10000;
  totalCustomers: number = 3500;
}
