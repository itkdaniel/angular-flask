import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { TextResponse } from '../models/textresponse.mode';
import { ChatgenService } from '../services/chatgen.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent {
  textList:TextResponse[]=[{sno:1,role:'',text:'',response:''}];
  // public data:TextResponse={sno:1,role:'',text:'',response:''};
  constructor (private chatgenService: ChatgenService, private router: Router) {}

  sanitycheck(data:TextResponse) {
    this.chatgenService.pingpong(data).subscribe(response => {
      console.log(`sanitycheck: ${JSON.stringify(response)}`)
      data.response = JSON.stringify(response);
    })
  }

  generateText(data:TextResponse) {
    console.log(data);
    this.chatgenService.genchat(data).subscribe(response => {
      console.log(`response: ${JSON.stringify(response)}`)
      data.response = response.response;
      if(this.textList.length>=data.sno){
            this.textList.push({sno:1,role:'',text:'',response:''});
            this.textList.push(response)
          }
    })
  }
  // generateText(data:TextResponse) {
  //   console.log(data)
  //   if(this.textList.length>=data.sno){
  //     this.textList.push({sno:1,role:'',text:'',response:''});
  //   }
    // this.openaiService.generateText(data.text).then(text => {
    //   data.response = text;
    //   if(this.textList.length===data.sno){
    //     this.textList.push({sno:1,text:'',response:''});
    //   }
    // }
}
