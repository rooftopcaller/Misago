# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ForumRole.special_role'
        db.add_column(u'forums_forumrole', 'special_role',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ForumRole.special_role'
        db.delete_column(u'forums_forumrole', 'special_role')


    models = {
        u'acl.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pickled_permissions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'forums.forum': {
            'Meta': {'object_name': 'Forum'},
            'archive_pruned_in': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pruned_archive'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['forums.Forum']"}),
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_as_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['forums.Forum']"}),
            'posts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'posts_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'prune_replied_after': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'prune_started_after': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'redirect_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'redirects_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'special_role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'threads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'threads_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'forums.forumrole': {
            'Meta': {'object_name': 'ForumRole'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pickled_permissions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'forums.roleforumacl': {
            'Meta': {'object_name': 'RoleForumACL'},
            'forum': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['forums.Forum']"}),
            'forum_role': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['forums.ForumRole']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('mptt.fields.TreeForeignKey', [], {'related_name': "'forums_acls'", 'to': u"orm['acl.Role']"})
        }
    }

    complete_apps = ['forums']