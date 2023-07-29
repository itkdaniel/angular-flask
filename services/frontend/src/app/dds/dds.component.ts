import { Component, ElementRef, Renderer2, ViewChild } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
// import { DatePickerComponent } from '@syncfusion/ej2-angular-calendars';

@Component({
  selector: 'app-dds',
  templateUrl: './dds.component.html',
  styleUrls: ['./dds.component.css']
})
export class DdsComponent {
  
  constructor (private fb: FormBuilder, private renderer: Renderer2) {}
  
  @ViewChild('dob')
  dob!: ElementRef<HTMLInputElement>;

  @ViewChild('g')
  g!: ElementRef<HTMLSelectElement>;
  
  // @ViewChild('age')
  // ageval!: ElementRef<HTMLInputElement>;
  gender:string = "Choose...";
  
  attributes = {
    'disabled': true,
    'value': this.dob
  };

  patientForm = this.fb.group({
    firstName: ['', Validators.required],
    lastName: ['', Validators.required],
    dateofbirth: ['', Validators.required],
    age: ['', Validators.required],
    ssn: ['', Validators.required],
    gender: ['', Validators.required],
    ethnicity: ['', Validators.required],
    address: this.fb.group({
      street: ['', Validators.required],
      city: ['', Validators.required],
      state: ['', Validators.required],
      zipcode: ['', Validators.required]
    }),
  });
  
  get firstName() { return this.patientForm.get("firstName"); }
  get lastName() { return this.patientForm.get("lastName"); }
  get dateofbirth() { return this.patientForm.get("dateofbirth"); }
  get age() { return this.patientForm.get("age"); }

  showPicker() {
    try{
      this.dob.nativeElement.showPicker();
    }catch(error) {
      // console.error(error);
    }
  }
  
  onSubmit() {
    console.log(`date: ${this.dob}`);
    console.log(this.lastName?.value);
  }

  private calcAge(date:any) {
    const d:Date = new Date(date);
    const t = new Date();
    // var age = t.getFullYear() - d.getFullYear();
    // let nage = ((t.getMonth() - d.getMonth() > 0) && (t.getDate() - d.getDate() > 0)) ? age : age-1;
    var age:number = Math.floor(Math.abs(t.getTime() - d.getTime()) / (1000*3600*24)/365);
    return age;
  }

  onChangeEvent(event: any){
    this.dob = event.target.value;
    let age = this.calcAge(this.dob);
    // this.ageval = age;
    this.age?.setValue(age.toString());
    console.log(`age: ${age}`);
    console.log(this.formatDate(this.dob));
  }

  private formatDate(date:any) {
    const d = new Date(date);
    let month = '' + (d.getMonth() + 1);
    let day = '' + (d.getDate() + 1);
    const year = d.getFullYear();
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    return [month, day, year].join('-');
  }


}
