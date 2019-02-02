import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { SearchResult } from './search/search.component'
@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor() { }x

  getSearchResults(search: string, amount: number): Observable<SearchResult[]> {
    var res: SearchResult[]  = []
    res.push(
      {
        url: "test.url.1",
        summary: "this is a summary",
        expanded: false
      })
      res.push(
      {
        url: "test.url.2",
        summary: "this is a summary",
        expanded: false
      })
      res.push(
      {
        url: "test.url.3",
        summary: "this is a summary",
        expanded: false
      })
      res.push(
      {
        url: "test.url.4",
        summary: "this is a summary",
        expanded: false
      })
      return of(res);
  }

  expandSearch(result: SearchResult): Observable<SearchResult> {

    result.summary = "This is a longer summary it is so much more";
    result.expanded = true;
    return of(result)
  }
}

