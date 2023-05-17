import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { Exam } from '../models/exam.mode';
import { ExamsApiService } from '../services/exams-api.service';

@Component({
  selector: 'app-exam-list',
  templateUrl: './exam-list.component.html',
  styleUrls: ['./exam-list.component.css']
})
export class ExamListComponent {
  examsList: Exam[] = [];

  constructor(private examsApi: ExamsApiService) {}

  ngOnInit() {
    this.getExams();
  }

  getExams() {
    this.examsApi.getExams()
    .subscribe(res => this.examsList = res);
  }
}
