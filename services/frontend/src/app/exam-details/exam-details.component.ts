import { Component } from '@angular/core';
import { Exam } from '../models/exam.mode';
import { ActivatedRoute } from '@angular/router';
import { ExamsApiService } from '../services/exams-api.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-exam-details',
  templateUrl: './exam-details.component.html',
  styleUrls: ['./exam-details.component.css']
})
export class ExamDetailsComponent {
  exam: Exam | undefined;
  json_exam = {};
  constructor (private route: ActivatedRoute, private examService: ExamsApiService, private location: Location) {}

  private getExam(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.examService.getExam(id).subscribe(data => {
      this.exam = data;
      this.json_exam = JSON.stringify(this.exam);
      console.log(`exam details: ${JSON.stringify(this.exam)}`);});
  }
  
  ngOnInit() {
    this.getExam();
  }
}
