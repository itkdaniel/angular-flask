import { Component } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { ExamsApiService } from '../services/exams-api.service';
import { Exam } from '../models/exam.mode';

@Component({
  selector: 'app-add-exam',
  templateUrl: './add-exam.component.html',
  styleUrls: ['./add-exam.component.css']
})
export class AddExamComponent {
  constructor (private fb: FormBuilder, private examService: ExamsApiService) {}

  examForm = this.fb.group({
    title: ['', Validators.required],
    description: ['', Validators.required]
  })

  get title() { return this.examForm.get('title'); }
  get description() { return this.examForm.get('description'); }
  
  onSubmit () {
    console.log(this.examForm);
    if (this.examForm.invalid){
      alert('Please fill out exam details');
    } else {
        this.examService.addExam(this.title?.value, this.description?.value).subscribe(data => {
          console.log(`data: ${JSON.stringify(data)}`);
          console.log(`id: ${data.id},title: ${data.title}`);
          console.log(`created_at: ${data.created_at}`);
        });
      console.log("examForm: " + this.examForm.value);
    }
  }
}
