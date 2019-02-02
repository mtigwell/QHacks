import { Component, OnInit } from '@angular/core';
import {FormGroup, FormBuilder, Validators } from '@angular/forms';
import { _localeFactory } from '@angular/core/src/application_module';
import { SearchService } from '../search.service';
import { saveAs } from "file-saver";

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})


export class SearchComponent implements OnInit {

  form: FormGroup;
  searchResults: SearchResult[] = [];
  search_name: string;
  essay: boolean; 
  
  constructor(private formBuilder: FormBuilder, private searchService: SearchService) { }

  ngOnInit() {
    this.form = this.formBuilder.group({
      search: [null, [Validators.required]],
      resultNum: [5, Validators.required],
      essayCount: [null, null]
    });
  }
  search() {
    if(this.essay){
      this.essay = false;
      this.genEssay()
    }
    else {
    var search = this.form.controls['search'];
    this.search_name = search.value;
    var numResult =  this.form.controls['resultNum'];
    if (search.valid && numResult.valid){
      console.log("SEARCHING.......");
      this.searchService.getSearchResults(search.value, numResult.value)
        .subscribe(result => {
          console.log(result);
          
          this.searchResults = result}
          );
    }
  }
  }

  genEssay() {
    var search = this.form.controls['search'];
    this.search_name = search.value;
    var numResult =  this.form.controls['resultNum'];
    var essayCount =  this.form.controls['essayCount'];
    if (search.valid && numResult.valid){
      console.log("GENERATING.......");
      this.searchService.genEssay(search.value, numResult.value, essayCount.value)
        .subscribe(result => {
          console.log(result);
          this.searchResults = result}
          );
    }
  }

  expandResult(result: SearchResult) {
    console.log("EXPANDING......");
    var index = this.searchResults.indexOf(result);
    this.searchService.expandSearch(result)
        .subscribe(responce => {
          this.searchResults[index].summary = responce;
        });
  }

  saveFile(){
    console.log('DOWNLOADING.......');
    
    let summary_file : string[] = []
    this.searchResults.forEach(element => {
      summary_file.push("URL:" + element.url + "\n");
      summary_file.push("Summary:\n" + element.summary + "\n");
    })
    let blob = new Blob(summary_file, {type: "text/plain;charset=utf-8"});
    saveAs(blob, this.search_name + "_summary.doc");
  }
}

export class SearchResult {
  url: string;
  summary: string;
  expanded: boolean;
}