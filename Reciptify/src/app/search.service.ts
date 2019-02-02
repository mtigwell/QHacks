import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { SearchResult } from './search/search.component';
import { HttpClient, HttpParams } from '@angular/common/http';
import { map } from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  res: SearchResult[]  = [];

  constructor(private httpClient: HttpClient) { }

  getSearchResults(search: string, amount: number): Observable<SearchResult[]> {
    var test;
    
    const params = new HttpParams({
      fromObject: {
        search: search,
        results: String(amount),
      }
    });
    
    return this.httpClient.get('http://127.0.0.1:5000/search', { params: params }).pipe(
      map(data  => {  
      let d : Array<any> =  Array(data)[0];
      this.res = []
      for ( let element of d){
        this.res.push({
          url: element['url'],
          summary: element['summary'],
          expanded: false
        })
      }
      return this.res
    }))
  }

  expandSearch(result: SearchResult): Observable<string> {
    const params = new HttpParams({
      fromObject: {
        url: result.url
      }
    });
    
    return this.httpClient.get('http://127.0.0.1:5000/expand', { params: params }).pipe(
      map(data  => {  
      return data['summary']
    }))
  }
}

