import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment.development';
import { Observable } from 'rxjs';
import { PopularProduct } from '../models/endpoint-specific/popular-product';

@Injectable({
  providedIn: 'root',
})
export class PopularProductsService {
  private apiUrl: string = environment.apiUrl + '/popular-products/';

  constructor(private http: HttpClient) {}

  getPopularProducts(): Observable<PopularProduct[]> {
    return this.http.get<PopularProduct[]>(this.apiUrl);
  }
}
