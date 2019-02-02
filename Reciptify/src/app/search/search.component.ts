import { Component, OnInit } from '@angular/core';
import {FormGroup, FormBuilder, Validators } from '@angular/forms';
import { _localeFactory } from '@angular/core/src/application_module';
import { SearchService } from '../search.service'

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})


export class SearchComponent implements OnInit {

  form: FormGroup;
  searchResults: SearchResult[] = [];
  
  constructor(private formBuilder: FormBuilder, private searchService: SearchService) { }

  ngOnInit() {
    this.form = this.formBuilder.group({
      search: [null, [Validators.required]],
      resultNum: [5, Validators.required],
    });
  }
  search() {
    var search = this.form.controls['search'];
    var numResult =  this.form.controls['resultNum'];
    if (search.valid && numResult.valid){
      console.log("SEARCHING.......");
      this.searchService.getSearchResults(search.value, numResult.value)
        .subscribe(result => this.searchResults = result);
        
    }
  }

  expandResult(result: SearchResult) {
    console.log("EXPANDING......");
    var index = this.searchResults.indexOf(result);
    this.searchService.expandSearch(result)
        .subscribe(responce => {
          this.searchResults[index] = responce;
        });
  }
}

export class SearchResult {
  url: string;
  summary: string;
  expanded: boolean;
}