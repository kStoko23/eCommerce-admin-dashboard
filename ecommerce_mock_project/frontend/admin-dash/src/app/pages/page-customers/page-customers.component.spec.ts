import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageCustomersComponent } from './page-customers.component';

describe('PageCustomersComponent', () => {
  let component: PageCustomersComponent;
  let fixture: ComponentFixture<PageCustomersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PageCustomersComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PageCustomersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
