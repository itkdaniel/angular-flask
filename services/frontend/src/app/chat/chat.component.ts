import { Component, ElementRef, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { TextResponse } from '../models/textresponse.mode';
import { ChatgenService } from '../services/chatgen.service';
import { CdkVirtualScrollViewport } from '@angular/cdk/scrolling';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
})

export class ChatComponent {
  public textList:TextResponse[]=[{"sno":1,"role":"user","text":"testing","response":""},{"sno":1,"role":"assistant","text":"testing","response":"something helpful..."}]
  public data:TextResponse = {"sno":1,"role":"user","text":"","response":""}
  public data$:TextResponse = {"sno":1,"role":"user","text":"⌚️ 📱 📲 💻 ⌨️ 🖥 🖨 🖱 🖲 🕹 🗜 💽 💾 💿 📀 📼 📷 📸 📹 🎥 📽 🎞 📞 ☎️ 📟 📠 📺 📻 🎙 🎚 🎛 🧭 ⏱ ⏲ ⏰ 🕰 ⌛️ ⏳ 📡 🔋 🪫 🔌 💡 🔦 🕯 🪔 🧯 🛢 🛍️ 💸 💵 💴 💶 💷 🪙 💰 💳 💎 ⚖️ 🪮 🪜 🧰 🪛 🔧 🔨 ⚒ 🛠 ⛏ 🪚 🔩 ⚙️ 🪤 🧱 ⛓ 🧲 🔫 💣 🧨 🪓 🔪 🗡 ⚔️ 🛡 🚬 ⚰️ 🪦 ⚱️ 🏺 🔮 📿 🧿 🪬 💈 ⚗️ 🔭 🔬 🕳 🩹 🩺 🩻 🩼 💊 💉 🩸 🧬 🦠 🧫 🧪 🌡 🧹 🪠 🧺 🧻 🚽 🚰 🚿 🛁 🛀 🧼 🪥 🪒 🧽 🪣 🧴 🛎 🔑 🗝 🚪 🪑 🛋 🛏 🛌 🧸 🪆 🖼 🪞 🪟 🛍 🛒 🎁 🎈 🎏 🎀 🪄 🪅 🎊 🎉 🪩 🎎 🏮 🎐 🧧 ✉️ 📩 📨 📧 💌 📥 📤 📦 🏷 🪧 📪 📫 📬 📭 📮 📯 📜 📃 📄 📑 🧾 📊 📈 📉 🗒 🗓 📆 📅 🗑 🪪 📇 🗃 🗳 🗄 📋 📁 📂 🗂 🗞 📰 📓 📔 📒 📕 📗 📘 📙 📚 📖 🔖 🧷 🔗 📎 🖇 📐 📏 🧮 📌 📍 ✂️ 🖊 🖋 ✒️ 🖌 🖍 📝 ✏️ 🔍 🔎 🔏 🔐 🔒 🔓 This shoud show all the emojis as emoji code ok here they are : 😀 😃 😄 😁 😆 😅 😂 🤣 🥲 🥹 ☺️ 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🥸 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁☹️ 😣 😖 😫 😩 🥺 😢 😭 😮‍💨 😤 😠 😡 🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🫣 🤗 🫡 🤔 🫢 🤭 🤫 🤥 😶 😶‍🌫️ 😐 😑 😬 🫨 🫠 😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 😵‍💫 🫥 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡 💩 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾","response":""}

  date = new Date();
  time = this.date.toLocaleTimeString();
  constructor (private chatgenService: ChatgenService, private router: Router) {}

  @ViewChild('CdkVirtualScrollViewport')
  virtualScrollViewport!:CdkVirtualScrollViewport;


  sanitycheck(data:TextResponse) {
    this.chatgenService.pingpong(data).subscribe(response => {
      console.log(`sanitycheck: ${JSON.stringify(response)}`)
      data.response = JSON.stringify(response);
    })
  }

  // generateText(data:TextResponse) {
  //   console.log(data);
  //   this.chatgenService.genchat(data).subscribe(response => {
  //     console.log(`response: ${JSON.stringify(response)}`)
  //     data.response = response.response;
  //     this.textList.push(data)
  //     this.textList.push(response)
  //     this.data = {"sno":1,"role":"","text":"","response":""}
  //     if(this.textList.length>=data.sno){
  //           // this.textList.push({sno:1,role:'',text:'',response:''});
  //           // this.textList.push(response)
  //           console.log(`textList: ${JSON.stringify(this.textList)}`)
  //         }
  //   })
  // }

  private _scrollToBottom() {
    setTimeout(() => {
      this.virtualScrollViewport.scrollToIndex(
        this.textList.length - 1
      );
      setTimeout(() => {
        const items = document.getElementsByClassName("app-chat");
        items[items.length - 1]?.scrollIntoView();
        console.log(`items length: ${items.length-1}`)
      }, 10);
    });
  }

  generateText(data:TextResponse) {
    console.log(`${data}`);
    console.log(data);
    // console.log(`response: ${JSON.stringify(response)}`)
    var response = {"sno":1,"role":"assistant","text":`${data.text}`,"response":"<blockquote>This is an <code>🤓 😎<strong><i>automatic response 🥶</i></strong></code> as an <b>artificially intelligent <code><i>AGI 🤖</i></code></b> (<p><small><i>Artificial General Intelligence 👽</i></small></p>). Please <small style='cursor: pointer;'><kbd><kbd>➢</kbd>connect</kbd></small> to the 💩 👻 API <u>  🎃 😺 ( <a href='#'>application programming interface</a> )</u> to test for a <mark>real response</mark>. Have a good day <footer class='blockquote-footer'>AI Model <cite title='gpt-3.5-turbo'>gpt-3.5-turbo🤑 😄 😁 😆😮‍💨</cite></footer></blockquote>"}
    data.response = response;
    this.textList.push(data)
    this.textList.push(response)
    this.data = {"sno":1,"role":"user","text":"","response":""}
    this.textList = [...this.textList]
    document.getElementById("prompt")?.focus()
    this._scrollToBottom();
    this.virtualScrollViewport.scrollTo({bottom: 0});
    // this.chatgenService.genchat(data).subscribe(response => {
    //   console.log(`response: ${JSON.stringify(response)}`)
    //   data.response = response.response;
    //   this.textList.push(data)
    //   this.textList.push(response)
    //   this.data = {"sno":1,"role":"","text":"","response":""}
    //   if(this.textList.length>=data.sno){
    //         this.textList.push({sno:1,role:'',text:'',response:''});
    //         this.textList.push(response)
    //         console.log(`textList: ${JSON.stringify(this.textList)}`)
    //       }
    // })
  }
}
