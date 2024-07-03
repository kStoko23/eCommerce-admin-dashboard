import { Routes } from '@angular/router';
import { PageDashboardComponent } from './pages/page-dashboard/page-dashboard.component';
import { PageCustomersComponent } from './pages/page-customers/page-customers.component';
import { PageSalesComponent } from './pages/page-sales/page-sales.component';
import { PageProductsComponent } from './pages/page-products/page-products.component';

export const routes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: PageDashboardComponent },
  { path: 'customers', component: PageCustomersComponent },
  { path: 'sales', component: PageSalesComponent },
  { path: 'products', component: PageProductsComponent },
];
