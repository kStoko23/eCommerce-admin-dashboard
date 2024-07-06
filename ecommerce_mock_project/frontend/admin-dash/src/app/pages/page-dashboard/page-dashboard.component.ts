import { Component } from '@angular/core';
import { CardComponent } from '../../shared/components/card/card.component';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { CustomersService } from '../../core/services/customers.service';
import { OrdersService } from '../../core/services/orders.service';
import { PopularProductsService } from '../../core/services/popular-products.service';
import { PopularProduct } from '../../core/models/endpoint-specific/popular-product';

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
  currentYear: number = new Date().getFullYear();

  popularProducts: PopularProduct[] = [];

  constructor(
    private customerService: CustomersService,
    private ordersService: OrdersService,
    private popularProductsService: PopularProductsService
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
    this.popularProductsService.getPopularProducts().subscribe({
      next: (data) => {
        this.popularProducts = data;
      },
      error: (error) => {
        console.error('Error fetching popular products', error);
      },
    });
  }
}
