import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map } from 'rxjs';
import { environment } from '../../../environments/environment.development';

@Injectable({
  providedIn: 'root',
})
export class OrdersService {
  private apiUrl = environment.apiUrl + '/count-orders/?time_period=last_year';

  constructor(private http: HttpClient) {}

  getOrdersCount(): Observable<number> {
    return this.http
      .get<{ orders_count: number }>(this.apiUrl)
      .pipe(map((response) => response.orders_count));
  }
}
