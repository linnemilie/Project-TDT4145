-- Gruppe 109 - Linn Emilie Kalleberg og Kirsten Gjester Nord



-- For å opprette ny database med tabeller: 

-- 1. sqlite3 db-name.db 
-- 2. .read create-tables.sql

create table jernbanestasjon (
  stasjonsnavn varchar(30) not null,
  antallMoh integer,
  constraint jernbanestasjon_pk primary key (stasjonsnavn)
);

create table banestrekning (
  strekningnavn varchar(30) not null,
  energitype varchar(30),
  startstasjon varchar(30) not null,
  endestasjon varchar(30) not null,
  constraint banestrekning_pk primary key (strekningnavn)
  constraint banestrekning_fk1 foreign key (startstasjon) references jernbanestasjon(stasjonsnavn) 
      on update cascade
      on delete cascade
  constraint banestrekning_fk2 foreign key (endestasjon) references jernbanestasjon(stasjonsnavn)
      on update cascade
      on delete cascade 
);

create table delstrekning (
  delstrekningnavn varchar(30) not null,
  lengde integer,
  sportype varchar(30),
  strekningnavn varchar(30),
  delstrekningFra varchar(30) not null,
  delstrekningTil varchar(30) not null,
  constraint delstrekning_pk primary key (delstrekningnavn)
  constraint delstrekning_fk1 foreign key (strekningnavn) references banestrekning(strekningnavn)
      on update cascade
      on delete cascade
  constraint delstrekning_fk2 foreign key (delstrekningFra) references jernbanestasjon(stasjonsnavn)
      on update cascade
      on delete cascade
  constraint delstrekning_fk3 foreign key (delstrekningTil) references jernbanestasjon(stasjonsnavn)
      on update cascade
      on delete cascade
);

create table togrute (
  rutenavn varchar(30) not null,
  strekningnavn varchar(30) not null,
  retning varchar(30),
  startstasjon varchar(30) not null,
  avgangstid time,
  endestasjon varchar(30) not null,
  ankomsttid time,
  operatørID integer not null,
  constraint togrute_pk primary key (rutenavn)
  constraint togrute_fk1 foreign key (strekningnavn) references banestrekning(strekningnavn)
      on update cascade
      on delete cascade
  constraint togrute_fk2 foreign key (startstasjon) references jernbanestasjon(stasjonsnavn)
      on update cascade
      on delete cascade
  constraint togrute_fk3 foreign key (endestasjon) references jernbanestasjon(stasjonsnavn)
      on update cascade
      on delete cascade
  constraint togrute_fk4 foreign key (operatørID) references operatør(operatørID)
      on update cascade
      on delete cascade
);

create table mellomstasjon (
  rutenavn varchar(30) not null,
  stasjonsnavn varchar(30) not null,
  ankomsttid time,
  avgangstid time,
  constraint mellomstasjon_pk primary key (rutenavn, stasjonsnavn)
  constraint mellomstasjon_fk1 foreign key (rutenavn) references togrute(rutenavn)
      on update cascade
      on delete cascade
  constraint mellomstasjon_fk2 foreign key (stasjonsnavn) references jernbanestasjon(stasjonsnavn)
      on update cascade
      on delete cascade
);

create table togreise (
  ukedag date not null,
  rutenavn varchar(30) not null,
  oppsettID integer not null,
  constraint togreise_pk primary key (ukedag, rutenavn)
  constraint togreise_fk1 foreign key (rutenavn) references togrute(rutenavn)
      on update cascade
      on delete cascade
  constraint togreise_fk2 foreign key (oppsettID) references vognoppsett(oppsettID)
      on update cascade
      on delete cascade
);

create table operatør (
  operatørID integer not null,
  operatørnavn varchar(30),
  constraint operatør_pk primary key (operatørID)
);

create table kunde (
  kundenummer integer not null,
  navn varchar(30),
  epost varchar(30),
  mobilnummer char(8),
  constraint kunde_pk primary key (kundenummer)
);

create table kunderegister (
  operatørID integer not null,
  kundenummer integer not null,
  constraint kunderegister_pk primary key (operatørID, kundenummer)
  constraint kunderegister_fk1 foreign key (operatørID) references operatør(operatørID)
      on update cascade
      on delete cascade
  constraint kunderegister_fk2 foreign key (kundenummer) references kunde(kundenummer)
      on update cascade
      on delete cascade
);

-- kan bruke select weekday({reisedato}) for å finne ukedag og dermed koble oss til en togreise

create table kundeordre (
  ordrenummer integer not null,
  bestillingsdato date,
  kundenummer int not null,
  startstasjon varchar(30) not null,
  endestasjon varchar(30) not null,
  constraint kundeordre_pk primary key (ordrenummer)
  constraint kundeordre_fk1 foreign key (kundenummer) references kunde(kundenummer)
      on update cascade
      on delete cascade
  constraint kundeordre_fk2 foreign key (startstasjon) references jernbanestasjon(stasjonsnavn)
      on update cascade
      on delete cascade
  constraint kundeordre_fk3 foreign key (endestasjon) references jernbanestasjon(stasjonsnavn)
      on update cascade
      on delete cascade
);

create table billettkjøp (
  billettID integer not null,
  ordrenummer integer not null,
  constraint kundeordre_pk primary key (billettID, ordrenummer)
  constraint kundeordre_fk1 foreign key (billettID) references billett(billettID)
      on update cascade
      on delete cascade
  constraint kundeordre_fk2 foreign key (ordrenummer) references kundeordre(ordrenummer)
      on update cascade
      on delete cascade
);

create table seteErOpptatt (
  billettID integer not null,
  opptattID integer not null,
  constraint seteErOpptatt_pk primary key (billettID, opptattID)
  constraint seteErOpptatt_fk1 foreign key (billettID) references billett(billettID)
      on update cascade
      on delete cascade
  constraint seteErOpptatt_fk2 foreign key (opptattID) references seteOpptatt(opptattID)
      on update cascade
      on delete cascade
);

create table seteOpptatt (
  opptattID integer not null,
  startstasjon varchar(30),
  endestasjon varchar(30),
  starttid time,
  endetid time,
  constraint seteOpptatt_pk primary key (opptattID)
  constraint seteOpptatt_fk1 foreign key (startstasjon) references jernbanestasjon(startstasjon)
      on update cascade
      on delete cascade
  constraint seteOpptatt_fk2 foreign key (endestasjon) references jernbanestasjon(endestasjon)
      on update cascade
      on delete cascade
);

create table billett (
  billettID integer not null,
  vognnummer integer,
  plassnummer integer,
  ukedag varchar(30) not null,
  rutenavn varchar(30) not null,
  reisedato date,
  constraint billett_pk primary key (billettID)
  constraint billett_fk1 foreign key (ukedag, rutenavn) references togreise(ukedag, rutenavn)
      on update cascade
      on delete cascade
);

create table vognoppsett (
  oppsettID integer not null,
  constraint vognoppsett_pk primary key (oppsettID)
);

create table vognIOppsett (
  oppsettID integer not null,
  vognID varchar not null,
  vognnummer integer,
  constraint vognIOppsett_pk primary key (oppsettID, vognID)
  constraint vognIOppsett_fk1 foreign key (oppsettID) references vognoppsett(oppsettID)
      on update cascade
      on delete cascade
  constraint vognIOppsett_fk2 foreign key (vognID) references vogn(vognID)
      on update cascade
      on delete cascade
);

create table vogn (
  vognID varchar not null,
  antallPlasser int,
  constraint vogn_pk primary key (vognID)
);
