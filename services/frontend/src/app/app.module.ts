import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ScrollingModule } from '@angular/cdk/scrolling';
// import { DatePickerModule } from '@syncfusion/ej2-angular-calendars';

import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ExamListComponent } from './exam-list/exam-list.component';
import { HttpClientModule } from '@angular/common/http';
import { ExamsApiService } from './services/exams-api.service';
import { HomePageComponent } from './home-page/home-page.component';
import { AddExamComponent } from './add-exam/add-exam.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ExamDetailsComponent } from './exam-details/exam-details.component';
import { RegisterComponent } from './register/register.component';
import { ExplorePageComponent } from './explore-page/explore-page.component';
import { ChatComponent } from './chat/chat.component';
import { HealthcheckComponent } from './healthcheck/healthcheck.component';
import { AuthService } from './services/auth.service';
import { HealthService } from './services/health.service';
import { ChatgenService } from './services/chatgen.service';
import { DdsComponent } from './dds/dds.component';
import { AttributeDirective } from './directives/attribute/attribute.directive';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    ExamListComponent,
    HomePageComponent,
    AddExamComponent,
    NavbarComponent,
    ExamDetailsComponent,
    RegisterComponent,
    ExplorePageComponent,
    ChatComponent,
    HealthcheckComponent,
    DdsComponent,
    AttributeDirective,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    ScrollingModule,
  ],
  providers: [
    ExamsApiService,
    AuthService,
    HealthService,
    ChatgenService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
