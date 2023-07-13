#!/usr/bin/env python3 
import click
@click.command()
def hello():
    click.echo('Hello World!')

@click.command()
def getLink():
    click.echo('크롤링을 원하시는 네이버 웹툰의 링크를 적어주세요:')

if __name__ == '__main__':
    getLink()