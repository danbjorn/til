---
created: 2021-04-27
tag: bitbucket
title: YAML anchors in Bitbucket Pipelines
---
I've been using Bitbucket Pipelines for quite some time now and I only just learned that
you can use YAML anchors in pipeline files.

I mostly know YAML anchors from [a nasty attack](https://en.wikipedia.org/wiki/Billion_laughs_attack)
but as I control the pipeline file, I don't have to be scared of that. Instead, I can
use them to significantly tidy up duplication. The most common use case I'll be using it
for is reusing test steps between environments.

The Bitbucket docs have a pretty good summary of the feature:
<https://support.atlassian.com/bitbucket-cloud/docs/yaml-anchors/>

As an addendum, I see that they have also improved support for private Docker images and
for custom pipes. Not perfect yet but honestly I still prefer Pipelines to Github
Actions.
