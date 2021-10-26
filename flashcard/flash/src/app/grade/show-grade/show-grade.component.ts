import { Component, OnInit } from '@angular/core';
import { SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-show-grade',
  templateUrl: './show-grade.component.html',
  styleUrls: ['./show-grade.component.css']
})
export class ShowGradeComponent implements OnInit {

  constructor(private service:SharedService) { }

  GradeList:any=[];

  ModalTitle:string;
  ActivateAddEditGradeComp:boolean="false";
  grade:any;
  ngOnInit(): void {

    this.refreshGradeList();
  }

  addClick(){
    this.grade{
      GradeId:0,
      GradeName:""

    }

    this.ModalTitle="Add Grade";
    this.ActivateAddEditGradeComp=true;
  }

  // editclick
  editClick(item){
    this.grade = item;
    this.ModalTitle='Edit Grade';
    this.ActivateAddEditGrade=true;
  }


  // close click
  closeClick(){
    this.ActivateAddEditGradeComp=false;
    this.refreshGradeList();
  }

  refreshGradeList(){
    this.service.getGradeList().subscribe(data=>{
      this.GradeList=data;
    });
  }
}
