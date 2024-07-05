import { Component } from '@angular/core';
import { CardComponent } from '../../shared/components/card/card.component';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { CustomersService } from '../../services/customers.service';
import { OrdersService } from '../../services/orders.service';

@Component({
  selector: 'app-page-dashboard',
  standalone: true,
  imports: [CardComponent, CommonModule, RouterLink],
  templateUrl: './page-dashboard.component.html',
  styleUrl: './page-dashboard.component.css',
})
export class PageDashboardComponent {
  totalOrders: number;
  totalCustomers: number;

  constructor(
    private customerService: CustomersService,
    private ordersService: OrdersService
  ) {}

  ngOnInit() {
    this.customerService.getCustomersCount().subscribe({
      next: (data) => {
        this.totalCustomers = data;
      },
      error: (error) => {
        console.error('Error fetching total customers', error);
      },
    });
    this.ordersService.getOrdersCount().subscribe({
      next: (data) => {
        this.totalOrders = data;
      },
      error: (error) => {
        console.error('Error fetching total customers', error);
      },
    });
  }
}
