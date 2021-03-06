#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'defaultstr'

from django import forms

sex_choices = (
    ('sex', u'性别'),
    ('male', u'男'),
    ('female', u'女'),
)
search_frequency_choices = (
    ('search_frequency', u'使用搜索引擎的频率'),
    ('frequently', u'每天使用多次'),
    ('usually', u'平均每天使用一次'),
    ('sometimes', u'每周偶尔使用两三次'),
    ('rarely', u'平均每周使用不超过一次'),
)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'请输入用户名',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'密码',
            }
        )
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        required=True,
        min_length=6,
        label=u'用户名',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'请输入用户名',
            }
        )
    )
    password = forms.CharField(
        required=True,
        min_length=6,
        label=u'密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'密码',
            }
        )
    )
    password_retype = forms.CharField(
        required=True,
        min_length=6,
        label=u'再次输入密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'再次输入密码',
            }
        )
    )
    email = forms.EmailField(
        required=True,
        label=u'邮箱',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'邮箱',
            }
        )
    )
    sex = forms.ChoiceField(
        required=True,
        choices=sex_choices,
        label=u'性别',
        widget=forms.Select(
            attrs={
                'class': 'select2-container form-control select select-primary',
            }
        )
    )
    search_frequency = forms.ChoiceField(
        required=True,
        choices=search_frequency_choices,
        label=u'搜索引擎使用频率',
        widget=forms.Select(
            attrs={
                'class': 'select2-container form-control select select-primary',
            }
        )
    )
    class_no = forms.CharField(
        required=True,
        label=u'班级',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'班级，如计92',
            }
        )
    )
    name = forms.CharField(
        required=True,
        label=u'真实姓名',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'真实姓名',
            }
        )
    )
    age = forms.IntegerField(
        required=True,
        label=u'年龄',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'年龄',
            }
        )
    )

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        password_retype = cleaned_data.get('password_retype')

        if password != password_retype:
            raise forms.ValidationError(
                u'两次输入密码不一致'
            )

        return cleaned_data


class EditInfoForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label=u'邮箱',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'输入邮箱',
            }
        )
    )
    sex = forms.ChoiceField(
        required=True,
        choices=sex_choices,
        widget=forms.Select(
            attrs={
                'class': 'select2-container form-control select select-primary'
            }
        )
    )
    class_no = forms.CharField(
        required=True,
        label=u'班级',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'请输入班级，如计92',
            }
        )
    )


class EditPasswordForm(forms.Form):

    cur_password = forms.CharField(
        required=True,
        min_length=6,
        label=u'当前密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'密码',
            }
        )
    )
    new_password = forms.CharField(
        required=True,
        min_length=6,
        label=u'新密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'密码',
            }
        )
    )
    new_password_retype = forms.CharField(
        required=True,
        min_length=6,
        label=u'再次输入密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'再次输入密码',
            }
        )
    )

    def clean(self):
        cleaned_data = super(EditPasswordForm, self).clean()
        password = cleaned_data.get('new_password')
        password_retype = cleaned_data.get('new_password_retype')

        if password != password_retype:
            raise forms.ValidationError(
                u'两次输入密码不一致'
            )

        return cleaned_data


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label=u'邮箱',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'输入邮箱',
            }
        )
    )


class ResetPasswordForm(forms.Form):

    new_password = forms.CharField(
        required=True,
        min_length=6,
        label=u'新密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'密码',
            }
        )
    )
    new_password_retype = forms.CharField(
        required=True,
        min_length=6,
        label=u'再次输入密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control login-field',
                'placeholder': u'再次输入密码',
            }
        )
    )

    def clean(self):
        cleaned_data = super(ResetPasswordForm, self).clean()
        password = cleaned_data.get('new_password')
        password_retype = cleaned_data.get('new_password_retype')

        if password != password_retype:
            raise forms.ValidationError(
                u'两次输入密码不一致'
            )

        return cleaned_data