import { ReciptifyPage } from './app.po';

describe('reciptify App', function() {
  let page: ReciptifyPage;

  beforeEach(() => {
    page = new ReciptifyPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
