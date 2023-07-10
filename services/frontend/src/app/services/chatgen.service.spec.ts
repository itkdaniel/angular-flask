import { TestBed } from '@angular/core/testing';

import { ChatgenService } from './chatgen.service';

describe('ChatgenService', () => {
  let service: ChatgenService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ChatgenService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
