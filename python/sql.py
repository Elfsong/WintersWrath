#coding:utf-8
import sys
import os

str_use = "use accenter;\n"

str_drop = 'drop table AC_ENTRY_GLOBAL_DEFAULT_$1 ;\n'

str_content = """
create table AC_ENTRY_GLOBAL_DEFAULT_$1 (
	CATEGORY_CODE VARCHAR2(32)  not null,
	ACCOUNT_NO VARCHAR2(20),
	DIRECTION VARCHAR2(4)  not null,
	ACCOUNT_DATE VARCHAR2(8)  not null,
	RECON_INST VARCHAR2(32)  not null,
	CURRENCY VARCHAR2(4)  not null,
	ACCOUNT_LOG_ID VARCHAR2(32)  not null,
	TRANS_LOG_ID VARCHAR2(32)  not null,
	DEBIT_AMOUNT NUMBER(15)  not null,
	CREDIT_AMOUNT NUMBER(15)  not null,
	TRANS_CODE VARCHAR2(4)  not null,
	SUB_TRANS_CODE VARCHAR2(6)  not null,
	INST_CHANNEL_API VARCHAR2(32),
	TRANS_DT TIMESTAMP(6)  not null,
	ORDER_NO VARCHAR2(128),
	OUT_BIZ_NO VARCHAR2(128),
	VOUCHER_ID VARCHAR2(32),
	ORIG_VOUCHER_ID VARCHAR2(32),
	MEMO VARCHAR2(256),
	OPERATOR VARCHAR2(32)  not null,
	GMT_CREATE TIMESTAMP(6)  not null,
	GMT_MODIFIED TIMESTAMP(6)  not null,
	ELIMINATE_ACCOUNT_LOG_ID VARCHAR2(32),
	ORIGINAL_DATE VARCHAR2(8),
	DEL_FLAG VARCHAR2(1),
	CORRECT_FLAG VARCHAR2(1),
	INST_ID VARCHAR2(16),
	PAY_INST_ID VARCHAR2(16),
	BALANCE NUMBER(15),
	END_TO_END_ID VARCHAR2(128),
	BIZ_PD_CODE VARCHAR2(21),
	BIZ_EV_CODE VARCHAR2(8),
	CNL_PD_CODE VARCHAR2(21),
	CNL_EV_CODE VARCHAR2(8),
	CNL_NO VARCHAR2(64),
	PD_CODE VARCHAR2(21),
	EV_CODE VARCHAR2(8)
);
"""
str_comment = """
comment on table AC_ENTRY_GLOBAL_DEFAULT_$1 is '财务标准的ALIPAY US机构会计分录表';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.CATEGORY_CODE is '归类码编号';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.ACCOUNT_NO is '账号';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.DIRECTION is '余额方向';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.ACCOUNT_DATE is '会计日';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.RECON_INST is '核算机构';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.CURRENCY is '币种';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.ACCOUNT_LOG_ID is '账务明细id';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.TRANS_LOG_ID is '记账凭证id';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.DEBIT_AMOUNT is '借方发生额';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.CREDIT_AMOUNT is '贷方发生额';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.TRANS_CODE is '交易代码';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.SUB_TRANS_CODE is '子交易代码';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.INST_CHANNEL_API is '清算渠道';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.TRANS_DT is '交易时间';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.ORDER_NO is '订单号';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.OUT_BIZ_NO is '外部订单号';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.VOUCHER_ID is '凭证号';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.ORIG_VOUCHER_ID is '原始凭证号';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.MEMO is '备注';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.OPERATOR is '操作员';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.GMT_CREATE is '创建时间';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.GMT_MODIFIED is '最后修改时间';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.ELIMINATE_ACCOUNT_LOG_ID is '冲正冲销账务流水号';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.ORIGINAL_DATE is '原记账时间';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.DEL_FLAG is '抹账标志[Y-deleted]';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.CORRECT_FLAG is '反交易和单边抹账区分，S-反交易，C-单边抹账';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.INST_ID is '银行简称';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.PAY_INST_ID is '打款银行简称';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.BALANCE is '余额';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.END_TO_END_ID is '端到端id';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.BIZ_PD_CODE is '直接驱动平台操作的业务产品代码，对应到平台接口上开的BizPdCode';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.BIZ_EV_CODE is '直接驱动平台操作的业务事件代码，对应到平台接口上开的BizEventCode';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.CNL_PD_CODE is '端到端传递的产品代码，对应eventContext里面的pdCode';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.CNL_EV_CODE is '端到端传递的事件代码，对应eventContext里面的pdEventCode';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.CNL_NO is '端到端流水号，对应eventcontext中的ChannelSeqNo';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.PD_CODE is '本次操作行为的产品代码，对应传输标准中的eventPdCode';
comment on column AC_ENTRY_GLOBAL_DEFAULT_$1.EV_CODE is '本次操作行为的事件代码，对应传输标准中的EventCode';
alter table AC_ENTRY_GLOBAL_DEFAULT_$1 add constraint PK_AC_ENTRY_GLOBAL_DEFAULT_$1 primary key (ACCOUNT_LOG_ID,ACCOUNT_DATE) using index;
create index IND_GLOBAL_DEFAULT_CATEGORY_DAILY on AC_ENTRY_GLOBAL_DEFAULT_$1 (ACCOUNT_DATE,DEL_FLAG,CATEGORY_CODE,CURRENCY,RECON_INST,DIRECTION,DEBIT_AMOUNT,CREDIT_AMOUNT) online;
"""

target_out = open('Table.sql', 'w')

for i in xrange(0,100):
	target_out.write(str_use)
	target_out.write( str_drop.replace('$1', str(i).zfill(2)) )
	target_out.write( str_content.replace('$1', str(i).zfill(2)) )
	target_out.write( str_comment.replace('$1', str(i).zfill(2)) )
	target_out.write( "-------------------------------------------------\n\n" )
