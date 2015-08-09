# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patch'
        db.create_table(u'server_patch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('platform', self.gf('django.db.models.fields.IntegerField')()),
            ('bild_tupe', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rivera', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lint', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('patch', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'server', ['Patch'])

        # Adding model 'TestGrop'
        db.create_table(u'server_testgrop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('libraries', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent_group', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('group_tupe', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rivera', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lint', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('patch', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'server', ['TestGrop'])

        # Adding model 'Test'
        db.create_table(u'server_test', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'server', ['Test'])

        # Adding M2M table for field group on 'Test'
        m2m_table_name = db.shorten_name(u'server_test_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('test', models.ForeignKey(orm[u'server.test'], null=False)),
            ('testgrop', models.ForeignKey(orm[u'server.testgrop'], null=False))
        ))
        db.create_unique(m2m_table_name, ['test_id', 'testgrop_id'])

        # Adding model 'TestSuitType'
        db.create_table(u'server_testsuittype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'server', ['TestSuitType'])

        # Adding model 'TestSuit'
        db.create_table(u'server_testsuit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('suit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['server.TestSuitType'])),
        ))
        db.send_create_signal(u'server', ['TestSuit'])

        # Adding M2M table for field test_group on 'TestSuit'
        m2m_table_name = db.shorten_name(u'server_testsuit_test_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('testsuit', models.ForeignKey(orm[u'server.testsuit'], null=False)),
            ('testgrop', models.ForeignKey(orm[u'server.testgrop'], null=False))
        ))
        db.create_unique(m2m_table_name, ['testsuit_id', 'testgrop_id'])

        # Adding model 'Configuration'
        db.create_table(u'server_configuration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['server.Patch'])),
            ('suit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['server.Test'])),
            ('setings', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'server', ['Configuration'])

        # Adding model 'TestResult'
        db.create_table(u'server_testresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['server.Test'])),
            ('test_conf_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['server.Configuration'])),
            ('result', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'server', ['TestResult'])

        # Adding model 'History'
        db.create_table(u'server_history', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_suit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['server.TestSuit'])),
            ('group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['server.TestGrop'])),
            ('test_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['server.Test'])),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'server', ['History'])


    def backwards(self, orm):
        # Deleting model 'Patch'
        db.delete_table(u'server_patch')

        # Deleting model 'TestGrop'
        db.delete_table(u'server_testgrop')

        # Deleting model 'Test'
        db.delete_table(u'server_test')

        # Removing M2M table for field group on 'Test'
        db.delete_table(db.shorten_name(u'server_test_group'))

        # Deleting model 'TestSuitType'
        db.delete_table(u'server_testsuittype')

        # Deleting model 'TestSuit'
        db.delete_table(u'server_testsuit')

        # Removing M2M table for field test_group on 'TestSuit'
        db.delete_table(db.shorten_name(u'server_testsuit_test_group'))

        # Deleting model 'Configuration'
        db.delete_table(u'server_configuration')

        # Deleting model 'TestResult'
        db.delete_table(u'server_testresult')

        # Deleting model 'History'
        db.delete_table(u'server_history')


    models = {
        u'server.configuration': {
            'Meta': {'object_name': 'Configuration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patch_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.Patch']"}),
            'setings': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'suit_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.Test']"})
        },
        u'server.history': {
            'Meta': {'object_name': 'History'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.TestGrop']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.Test']"}),
            'test_suit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.TestSuit']"})
        },
        u'server.patch': {
            'Meta': {'object_name': 'Patch'},
            'bild_tupe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'patch': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'platform': ('django.db.models.fields.IntegerField', [], {}),
            'rivera': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'server.test': {
            'Meta': {'object_name': 'Test'},
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['server.TestGrop']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'server.testgrop': {
            'Meta': {'object_name': 'TestGrop'},
            'group_tupe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libraries': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent_group': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'patch': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rivera': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'server.testresult': {
            'Meta': {'object_name': 'TestResult'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.TextField', [], {}),
            'test_conf_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.Configuration']"}),
            'test_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.Test']"}),
            'time': ('django.db.models.fields.DateField', [], {})
        },
        u'server.testsuit': {
            'Meta': {'object_name': 'TestSuit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'suit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.TestSuitType']"}),
            'test_group': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['server.TestGrop']", 'symmetrical': 'False'})
        },
        u'server.testsuittype': {
            'Meta': {'object_name': 'TestSuitType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['server']