#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from caldav.lib.namespace import ns
from base import BaseElement, ValuedBaseElement


## Operations
class Propfind(BaseElement):
    tag = ns("D", "propfind")


class PropertyUpdate(BaseElement):
    tag = ns("D", "propertyupdate")


class Mkcol(BaseElement):
    tag = ns("D", "mkcol")

## Filters

## Conditions

## Components / Data


class Prop(BaseElement):
    tag = ns("D", "prop")


class Collection(BaseElement):
    tag = ns("D", "collection")


class Set(BaseElement):
    tag = ns("D", "set")


## Properties
class ResourceType(BaseElement):
    tag = ns("D", "resourcetype")


class DisplayName(ValuedBaseElement):
    tag = ns("D", "displayname")


class SyncToken(BaseElement):
    tag = ns("D", "sync-token")

class SyncLevel(ValuedBaseElement):
    tag = ns("D", "sync-level")

class Href(BaseElement):
    tag = ns("D", "href")

class ETag(BaseElement):
    tag = ns("D", "getetag")

class Response(BaseElement):
    tag = ns("D", "response")


class Status(BaseElement):
    tag = ns("D", "status")

class CurrentUserPrincipal(BaseElement):
    tag = ns("D", "current-user-principal")

