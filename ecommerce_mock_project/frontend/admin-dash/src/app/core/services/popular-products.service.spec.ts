import { TestBed } from '@angular/core/testing';

import { PopularProductsService } from './popular-products.service';

describe('PopularProductsService', () => {
  let service: PopularProductsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PopularProductsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
