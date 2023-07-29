import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DdsComponent } from './dds.component';

describe('DdsComponent', () => {
  let component: DdsComponent;
  let fixture: ComponentFixture<DdsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DdsComponent]
    });
    fixture = TestBed.createComponent(DdsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
