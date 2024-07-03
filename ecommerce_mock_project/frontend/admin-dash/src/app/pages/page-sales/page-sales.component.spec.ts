import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageSalesComponent } from './page-sales.component';

describe('PageSalesComponent', () => {
  let component: PageSalesComponent;
  let fixture: ComponentFixture<PageSalesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PageSalesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PageSalesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
