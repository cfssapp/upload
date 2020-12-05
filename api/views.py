from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, ArticleSerializer

from .models import Task, Article
# Create your views here.

jsonData = [
    {
        "id": "fake-list-0",
        "owner": "付小小",
        "title": "Alipay",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/uMfMFlvUuceEyPpotzlq.png",
        "status": "active",
        "percent": 83,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
        "href": "https://ant.design",
        "updatedAt": 1607155074056,
        "createdAt": 1607155074056,
        "subDescription": "那是一种内在的东西， 他们到达不了，也无法触及的",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 144426,
        "newUser": 1421,
        "star": 148,
        "like": 194,
        "message": 17,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-1",
        "owner": "曲丽丽",
        "title": "Angular",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iZBVOIhGJiAnhplqjvZW.png",
        "status": "exception",
        "percent": 79,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png",
        "href": "https://ant.design",
        "updatedAt": 1607147874056,
        "createdAt": 1607147874056,
        "subDescription": "希望是一个好东西，也许是最好的，好东西是不会消亡的",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 183261,
        "newUser": 1114,
        "star": 141,
        "like": 157,
        "message": 17,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-2",
        "owner": "林东东",
        "title": "Ant Design",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iXjVmWVHbCJAyqvDxdtx.png",
        "status": "normal",
        "percent": 59,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png",
        "href": "https://ant.design",
        "updatedAt": 1607140674057,
        "createdAt": 1607140674057,
        "subDescription": "生命就像一盒巧克力，结果往往出人意料",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 130955,
        "newUser": 1063,
        "star": 174,
        "like": 128,
        "message": 17,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-3",
        "owner": "周星星",
        "title": "Ant Design Pro",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/gLaIAoVWTtLbBWZNYEMg.png",
        "status": "active",
        "percent": 85,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png",
        "href": "https://ant.design",
        "updatedAt": 1607133474057,
        "createdAt": 1607133474057,
        "subDescription": "城镇中有那么多的酒馆，她却偏偏走进了我的酒馆",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 114258,
        "newUser": 1499,
        "star": 141,
        "like": 195,
        "message": 12,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-4",
        "owner": "吴加好",
        "title": "Bootstrap",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/gLaIAoVWTtLbBWZNYEMg.png",
        "status": "exception",
        "percent": 66,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png",
        "href": "https://ant.design",
        "updatedAt": 1607126274057,
        "createdAt": 1607126274057,
        "subDescription": "那时候我只会想自己想要什么，从不想自己拥有什么",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 163795,
        "newUser": 1618,
        "star": 148,
        "like": 119,
        "message": 11,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-5",
        "owner": "朱偏右",
        "title": "React",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iXjVmWVHbCJAyqvDxdtx.png",
        "status": "normal",
        "percent": 76,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png",
        "href": "https://ant.design",
        "updatedAt": 1607119074057,
        "createdAt": 1607119074057,
        "subDescription": "那是一种内在的东西， 他们到达不了，也无法触及的",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 175043,
        "newUser": 1838,
        "star": 154,
        "like": 151,
        "message": 11,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-6",
        "owner": "鱼酱",
        "title": "Vue",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ComBAopevLwENQdKWiIn.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iZBVOIhGJiAnhplqjvZW.png",
        "status": "active",
        "percent": 85,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/ComBAopevLwENQdKWiIn.png",
        "href": "https://ant.design",
        "updatedAt": 1607111874057,
        "createdAt": 1607111874057,
        "subDescription": "希望是一个好东西，也许是最好的，好东西是不会消亡的",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 188892,
        "newUser": 1586,
        "star": 197,
        "like": 147,
        "message": 17,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-7",
        "owner": "乐哥",
        "title": "Webpack",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/nxkuOJlFJuAUhzlMTCEe.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/uMfMFlvUuceEyPpotzlq.png",
        "status": "exception",
        "percent": 56,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/nxkuOJlFJuAUhzlMTCEe.png",
        "href": "https://ant.design",
        "updatedAt": 1607104674057,
        "createdAt": 1607104674057,
        "subDescription": "生命就像一盒巧克力，结果往往出人意料",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 114032,
        "newUser": 1811,
        "star": 142,
        "like": 163,
        "message": 18,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-8",
        "owner": "谭小仪",
        "title": "Alipay",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/uMfMFlvUuceEyPpotzlq.png",
        "status": "normal",
        "percent": 71,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
        "href": "https://ant.design",
        "updatedAt": 1607097474057,
        "createdAt": 1607097474057,
        "subDescription": "城镇中有那么多的酒馆，她却偏偏走进了我的酒馆",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 120038,
        "newUser": 1817,
        "star": 129,
        "like": 133,
        "message": 14,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-9",
        "owner": "仲尼",
        "title": "Angular",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iZBVOIhGJiAnhplqjvZW.png",
        "status": "active",
        "percent": 95,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png",
        "href": "https://ant.design",
        "updatedAt": 1607090274057,
        "createdAt": 1607090274057,
        "subDescription": "那时候我只会想自己想要什么，从不想自己拥有什么",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 165493,
        "newUser": 1358,
        "star": 164,
        "like": 119,
        "message": 13,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-10",
        "owner": "付小小",
        "title": "Ant Design",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iXjVmWVHbCJAyqvDxdtx.png",
        "status": "exception",
        "percent": 71,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png",
        "href": "https://ant.design",
        "updatedAt": 1607083074057,
        "createdAt": 1607083074057,
        "subDescription": "那是一种内在的东西， 他们到达不了，也无法触及的",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 114297,
        "newUser": 1783,
        "star": 197,
        "like": 103,
        "message": 11,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-11",
        "owner": "曲丽丽",
        "title": "Ant Design Pro",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/gLaIAoVWTtLbBWZNYEMg.png",
        "status": "normal",
        "percent": 52,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png",
        "href": "https://ant.design",
        "updatedAt": 1607075874057,
        "createdAt": 1607075874057,
        "subDescription": "希望是一个好东西，也许是最好的，好东西是不会消亡的",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 132848,
        "newUser": 1362,
        "star": 186,
        "like": 176,
        "message": 19,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-12",
        "owner": "林东东",
        "title": "Bootstrap",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/gLaIAoVWTtLbBWZNYEMg.png",
        "status": "active",
        "percent": 62,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png",
        "href": "https://ant.design",
        "updatedAt": 1607068674057,
        "createdAt": 1607068674057,
        "subDescription": "生命就像一盒巧克力，结果往往出人意料",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 180632,
        "newUser": 1199,
        "star": 199,
        "like": 193,
        "message": 16,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-13",
        "owner": "周星星",
        "title": "React",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iXjVmWVHbCJAyqvDxdtx.png",
        "status": "exception",
        "percent": 82,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png",
        "href": "https://ant.design",
        "updatedAt": 1607061474057,
        "createdAt": 1607061474057,
        "subDescription": "城镇中有那么多的酒馆，她却偏偏走进了我的酒馆",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 102785,
        "newUser": 1510,
        "star": 171,
        "like": 200,
        "message": 12,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-14",
        "owner": "吴加好",
        "title": "Vue",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ComBAopevLwENQdKWiIn.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iZBVOIhGJiAnhplqjvZW.png",
        "status": "normal",
        "percent": 88,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/ComBAopevLwENQdKWiIn.png",
        "href": "https://ant.design",
        "updatedAt": 1607054274057,
        "createdAt": 1607054274057,
        "subDescription": "那时候我只会想自己想要什么，从不想自己拥有什么",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 135642,
        "newUser": 1426,
        "star": 125,
        "like": 182,
        "message": 17,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-15",
        "owner": "朱偏右",
        "title": "Webpack",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/nxkuOJlFJuAUhzlMTCEe.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/uMfMFlvUuceEyPpotzlq.png",
        "status": "active",
        "percent": 58,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/nxkuOJlFJuAUhzlMTCEe.png",
        "href": "https://ant.design",
        "updatedAt": 1607047074057,
        "createdAt": 1607047074057,
        "subDescription": "那是一种内在的东西， 他们到达不了，也无法触及的",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 193619,
        "newUser": 1800,
        "star": 141,
        "like": 179,
        "message": 13,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-16",
        "owner": "鱼酱",
        "title": "Alipay",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/uMfMFlvUuceEyPpotzlq.png",
        "status": "exception",
        "percent": 81,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
        "href": "https://ant.design",
        "updatedAt": 1607039874057,
        "createdAt": 1607039874057,
        "subDescription": "希望是一个好东西，也许是最好的，好东西是不会消亡的",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 105318,
        "newUser": 1348,
        "star": 122,
        "like": 181,
        "message": 19,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-17",
        "owner": "乐哥",
        "title": "Angular",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iZBVOIhGJiAnhplqjvZW.png",
        "status": "normal",
        "percent": 71,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png",
        "href": "https://ant.design",
        "updatedAt": 1607032674057,
        "createdAt": 1607032674057,
        "subDescription": "生命就像一盒巧克力，结果往往出人意料",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 147361,
        "newUser": 1520,
        "star": 144,
        "like": 200,
        "message": 19,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-18",
        "owner": "谭小仪",
        "title": "Ant Design",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/iXjVmWVHbCJAyqvDxdtx.png",
        "status": "active",
        "percent": 56,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png",
        "href": "https://ant.design",
        "updatedAt": 1607025474057,
        "createdAt": 1607025474057,
        "subDescription": "城镇中有那么多的酒馆，她却偏偏走进了我的酒馆",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 147225,
        "newUser": 1688,
        "star": 117,
        "like": 153,
        "message": 20,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    },
    {
        "id": "fake-list-19",
        "owner": "仲尼",
        "title": "Ant Design Pro",
        "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png",
        "cover": "https://gw.alipayobjects.com/zos/rmsportal/gLaIAoVWTtLbBWZNYEMg.png",
        "status": "exception",
        "percent": 69,
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png",
        "href": "https://ant.design",
        "updatedAt": 1607018274057,
        "createdAt": 1607018274057,
        "subDescription": "那时候我只会想自己想要什么，从不想自己拥有什么",
        "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
        "activeUser": 193586,
        "newUser": 1876,
        "star": 136,
        "like": 189,
        "message": 14,
        "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
        "members": [
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                "name": "曲丽丽",
                "id": "member1"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                "name": "王昭君",
                "id": "member2"
            },
            {
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                "name": "董娜娜",
                "id": "member3"
            }
        ]
    }
]

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



@csrf_exempt
def article_list(request):
    """
    List all code articles, or create a new Article.
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)



    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)