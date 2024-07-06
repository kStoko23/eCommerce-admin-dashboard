import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map } from 'rxjs';
import { environment } from '../../../environments/environment.development';

@Injectable({
  providedIn: 'root',
})
export class CustomersService {
  private apiUrl =
    environment.apiUrl + '/count-customers/?time_period=last_year';

  constructor(private http: HttpClient) {}

  getCustomersCount(): Observable<number> {
    return this.http
      .get<{ customers_count: number }>(this.apiUrl)
      .pipe(map((response) => response.customers_count));
  }
}
